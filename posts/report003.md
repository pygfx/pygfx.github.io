# Looking back at 2025, and forward to 2026

<!-- DATE: 2026-02-12 -->
<!-- AUTHOR: Almar -->

In this post I look back at what we achieved in 2025, and where we want to go in 2026.


<!-- END_SUMMARY -->


## Overview of 2025

### PyGfx

We started the year with a big effor to refactor the rendering pipeline. This touched caching, scene traversal, managing 'scene environment', and a lot more. This work was spread over multiple pull requests, and was needed to allow more flexibility, such as having different blend modes for different materials.

This laid the foundations to refactor the blending mechanics, a big PR that took 4 months to finish, with several follow-up PRs to iron out the details.
In short, with these changes we acknowledge that blending is a hard problem for which there is no single best solution.
Instead of trying to solve it (badly) for the user, we give the user tools to handle blending in various ways. This inclused more control over blending order, transparency, and depth handling. But also provide alternative blending options like weighed blending and dithering.

Further notable improvements:

* A succession of optimisations to the transform systems.
* The text rendering underwent a refactor, to improve the performance and support multi-text labels, e.g. making the ruler object more efficient.
* The geometry object was made simpler, to just be an object that holds data, which simplifies the API and allowed for some performance improvements.
* The camera's ability to 'snap' on a scene was improved (`.show_object(... match_aspect=True)`), and some issues related to depth were fixed.
* Lines now support loops and infinite lines.
* Points can have per-vertex markers.
* There has been a lot of work (thanks to Pan) on support for gltf and physical rendering.
* We added post-processing effects, including two post-processing anti-aliasing filters
  (fxaa and our own ddaa), and the resolve pass when doing ssaa was improved. Overall
  this results in much crisper/cleaner images.


### wgpu-py

For wgpu-py we implemented improved support for type hints, making it easier to
write code using wgpu using IDE's that use static or dynamic introspection.

And of course we kept up with new versions of the WebGPU spec and wgpu-native.


### rendercanvas

The most notable improvements in rendercanvas are:

* Improved support for type hints.
* Higher-precision timers (to avoid lower FPS than expected on Windows).
* Improved scheduling, e.g. making sure that size-events are up-to-date.
* Similarly, events are processed as close as possible before rendering the next frame, which reduces any perceived lag for remote backends.
* Support for Pyodide; you can run rendercanvas in the browser! Thanks Jan!


### The road to async

Quite a lot of effort was put into improving the support for async. This work
was pretty hard, because it involves the (changing) API of wgpu-native to deal with asynchronous calls,
different async frameworks (e.g. asyncio, trio, rendercanvas' async adapter), and threading.

One notable advantage of async we were looking forward to was the improved performance of rendercanvas backends that need the rendered image as a bitmap, which is downloaded via `GPUBuffer.map_async()`.

To kick this work of, the context classes that were first implemented as part of `wgpu-py` were moved to `rendercanvas`. This made it possible in `rendercanvas` to implement more advanced contexts, and let wgpu-py focus on being a GPU API.

Then we applied several changes in rendercanvas and wgpu-py to allow them to interoperate in an async setting.

In rendercanvas:

* Provides `loop.call_soon_threadsafe()`.
* Loops have a much better defined lifecycle.
* Uses `sys.set_asyncgen_hooks` where appopriate (replacing the use of `sniffio`).

In wgpu-py:

* Runs a per-device thread to poll wgpu-core. This is lightweight while allowing to respond as quickly as possible when wgpu-core finishes an async call.
* Has a new `GPUPromise` class to handle the async mechanics, which exposes `.then()`.
* Uses 'sys.get_asyncgen_hooks' to detect the loop.
* Calls `loop.call_soon_threadsafe` from the polling thread to wake the main thread.

With these changes, it became possible to implement *async bitmap present*; the rendered image
can be downloaded from the GPU without actually waiting for it; the CPU (and GPU) can do other things while this happens. This results in a major increase in framerate.

This directly benefits the Jupyter backend and future remote backends, but also makes it viable to make
bitmap-present the default for Qt, which solves many issues our users were facing.


## What we did not get to

There were also features that we planned to do in 2025, but that we did not mange to do in 2025.

* The 'update propagation' work. The scheduling improvements and the async work laid the foundations, but we need to finish things in PyGfx, e.g. a new `View` class and async picking.
* Log plots and map projections.


## Outlook for 2026

More or less in order of urgency:

* An `Anywidget` backend in `rendercanvas`, allowing remote rendering in a wide range of applications (e.g. Jupyter, VSCode, Marimo notebooks, and more).
* Finish the `View` class and other work related to 'update propagation'.
* Log plots and map projections.
* Enabling and promoting using wgpu compute for scientific applications.
* Pyodide support for wgpu-py and PyGfx.
* We want to look into a more reliable backend for wgpu-py, either by giving wgpu-native a boost, hooking into wgpu-core directly, or switching to Dawn.
* Support for native widgets in `rendercanvas`, so it does not depend on an any external library to provide a window.
* Improvements to streaming in remote rendering (with `Anywidget`); we want to look into mpeg encoding and shaders that encode/decode  jpeg.

## Funding

In 2025 we received generous funding from the Flatiron Institute and from Ramona Optics. Together with some buildup runway in 2025 this helped us through 2025. We are very grateful for these funds; without these, PyGfx, wgpu-py and rendercanvas would probably be abandonware.

For 2026, both current sponsors continue to support PyGfx, although with smaller amounts. We also applied for a European grant, for which we passed the first round, and hope to hear the verdict soon.

Almar, Kushal, and Caitlin are also working on a proprietary project that uses PyGfx. Some of the work mentioned in the outlook will be done as part of that project.

If your company or research group is able to financially support this project, that would be awesome! We need funding to keep going. It looks like 2026 will be fine, but there have been times when I did not know how things would work out. So please reach out if you can!


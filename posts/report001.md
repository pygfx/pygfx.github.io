# Looking back at 2024

<!-- DATE: 2025-01-16 -->
<!-- AUTHOR: Almar -->

In this first post I look back at what we achieved in 2024.

<!-- END_SUMMARY -->


## Some history

Korijn and I (Almar) have been working on Pygfx since 2020.
At the time, the development of WebGPU and ([wgpu-native](https://github.com/gfx-rs/wgpu-native)) was just getting started. Both WebGPU and Pygfx have come a long way since then.
In an earlier [post](https://almarklein.org/wgpu.html) I describe the origins of Pygfx from a more technical perspective.

For several years, our work was funded by the company that Korijn was
employed with. But this ended in 2024 when his division was disbanded for
corporate reasons.

To keep Pygfx going, we came up with the sponsorship model presented at this website.
Since we (the developers of Pygfx) now need to answer to multiple stakeholders,
it seems like a good idea to write regular status reports.

The idea of posts like this, is to provide insight into the
higher level perspective, design decisions, priorities, and
achievements. I plan to write one every one or two months or so.


## Overview of 2024

From the start of 2024, our goal was to move to a "1.0 release". With
this we mean that we wanted to implement crucial features, and address
the issues/features that would introduce backwards incompatibilities.
We summarized this in [issue #932](https://github.com/pygfx/pygfx/issues/392).

I'll briefly discuss the biggest chunks of work that we did in 2024.


### Buffer and texture updates

In [pr #795](https://github.com/pygfx/pygfx/pull/795) and later PR's, we
refactored large parts of the buffer and texture objects for more efficient
updates. Later we introduced a way to send data to a buffer/texture without
it being stored on the CPU in [pr #879](https://github.com/pygfx/pygfx/pull/879).


### Async support

Async is a tricky topic. The WebGPU API specifies some functions as being
asynchronous. The main reason for wanting to adhere to this, is
that it would allow us to use JavaScript's WebGPU API, which is necessary
if we ever want to support Pyodide/PyScript and run in the browser.

The tricky part is that async code tends to force other code to be async too.
And we did not want to force async on our users.
In [wgpu-py](https://github.com/pygfx/wgpu-py/) we addressed this by providing both
sync and async flavours for such functions.
In the [rendercanvas](https://github.com/pygfx/rendercanvas) we implemented an
awesome event-loop mechanism that supports both sync and async callbacks.

What's left (to do in 2025) is to combine this in Pygfx.


### Rendercanvas

This year we also moved the GUI subpackage out of wgpu-py, into its own library: `rendercanvas`.
The subpackage was getting more complex, and giving it its own repo gives it room
to grow.

The purpose or `rendercanvas` is to provide a canvas/window/widget to
render to with WebGPU. Improvements made since it has its own repo include: support for
Asyncio and Trio, more consistent behavior across backends, async
support, and sigint handling.


### Update propagation

In [issue #495](https://github.com/pygfx/pygfx/issues/495) we outlined a set of changes related to how things react to changes and user input. The plan touches the event system in `rendercanvas`, and how to use this in Pygfx.
Part of this plan is to better separate rendering from handling updates. The renderer and world objects
should not participate in the event system.

This is an ongoing effort, with most of the work done in `rendercanvas`,
but quite some work ahead in Pygfx. The refactoring of the renderer / viewport as part of [issue #492](https://github.com/pygfx/pygfx/issues/492) is closely related to this work.


### Plotting support

We implemented improvements to text, ticks (`Ruler` object), and grids.
The viewport work is also a prerequisite for proper support for subplots.


### Mesh rendering

While Korijn and I focussed on the above, Pan has made a lot of contributions
related to advanced mesh rendering, like environment maps, PBR materials, animations,
compliance with the gltf format, and more.


## Up next

In the [next post](report002.html) I talk about what we plan to work on in 2025.

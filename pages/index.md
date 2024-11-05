<center>
<img src='pygfx1024.png' width='96px' height='96px' />
<span style='font-size:100px; position: relative; top: -20px; left: 10px;'>Pygfx</span><br>
<i style='font-size:110%;'>A powerful and reliable render engine for Python</i>


<img src='https://img.shields.io/badge/uses-webgpu-blue?style=flat'/>
<img src='https://img.shields.io/github/v/release/pygfx/pygfx?style=flat&label=version'/>
<img src='https://img.shields.io/github/stars/pygfx/pygfx?style=flat'/>

<p style='text-align:left; max-width:600px; margin: 2em 1em;'>
Pygfx (py-graphics) is built on WebGPU, enabling superior performance and reliability compared to OpenGL-based solutions. It is designed for simplicity and versatility: with its modular architecture, you can effortlessly assemble graphical scenes for diverse applications, from scientific visualization to video game rendering.
</p>


<a class='button' href='https://github.com/pygfx/pygfx'><i class='fab'></i> Source</a>
<a class='button' href='https://pygfx.readthedocs.io/stable/_gallery/index.html'><i class='fas'></i> Gallery</a>
<a class='button' href='https://pygfx.readthedocs.io'><i class='fas'></i> Documentation</a>
<a class='button yellow' href='sponsor.html'><i class='fas'></i> Support & Sponsoring</a>

</center>


## <i class='fas'></i> News

* `04-10-2024`  Released [wgpu-py v0.19.0](https://github.com/pygfx/wgpu-py/releases/tag/v0.19.0)
* `25-09-2024`  Released [pygfx v0.5.0](https://github.com/pygfx/pygfx/releases/tag/v0.5.0)


## <i class='fas'></i> Getting started

Pygfx runs almost anywhere, you don't need a fancy GPU.

* Install with ``pip install pygfx glfw``.
* Check out the [guide](https://docs.pygfx.org/stable/guide.html).
* Have a look at the examples in the [gallery](https://pygfx.readthedocs.io/stable/_gallery/index.html).


## <i class='fas'></i> Projects

The following projects fall under the pygfx.org umbrella:

<div class='project-container'>

    <div class=projectbox>
        <a class='button' href='https://pygfx.readthedocs.io'><i class='fas'></i> Docs</a>
        <a class='button' href='https://github.com/pygfx/pygfx'><i class='fab'></i> Source</a>
        <h3>Pygfx</h3>
        A powerful and reliable render engine for Python. The main project.
    </div>

    <div class=projectbox>
        <a class='button' href='https://wgpu-py.readthedocs.io'><i class='fas'></i> Docs</a>
        <a class='button' href='https://github.com/pygfx/wgpu-py'><i class='fab'></i> Source</a>
        <h3>wgpu-py</h3>
        WebGPU for Python. Pygfx uses this to control your GPU.
    </div>

    <div class=projectbox>
        <a class='button' href='https://rendercanvas.readthedocs.io'><i class='fas'></i> Docs</a>
        <a class='button' href='https://github.com/pygfx/rendercanvas'><i class='fab'></i> Source</a>
        <h3>RenderCanvas</h3>
        One canvas API, multiple backends. Enables Pygfx to
        render into an Qt/wx application, Jupyter notebook, and more.
    </div>

    <div class=projectbox>
        <a class='button' href='https://pylinalg.readthedocs.io'><i class='fas'></i> Docs</a>
        <a class='button' href='https://github.com/pygfx/pylinalg'><i class='fab'></i> Source</a>
        <h3>pylinalg</h3>
        Linear algebra utilities for Python. Used in Pygfx for its transform system.
    </div>
</div>

We also help maintain the following projects:

<div class='project-container'>
    <div class=projectbox>
        <a class='button' href='https://github.com/gfx-rs/wgpu-native'><i class='fab'></i> Source</a>
        <h3>wgpu-native</h3>
        Provides a C-API for WebGPU by implementing <i>webgpu.h</i>. Wrapped by wgpu-py.
    </div>

    <div class=projectbox>
        <a class='button' href='https://github.com/vispy/jupyter_rfb'><i class='fab'></i> Source</a>
        <h3>jupyter_rfb</h3>
        A remote frame-buffer for Jupyter. Enables Jupyter support in RenderCanvas.
    </div>
</div>


## <i class='fas'></i> Mission

We are dedicated to bring powerful and reliable visualization to the Python world.
We believe that WebGPU is the future for graphics and bring it to Python with the wgpu-py library. On top of that, we build Pygfx: a modern, versatile, and Pythonic rendering engine.

Pygfx provides a basis on top of which a multitude of visualizations become possible. From applications to libraries, from games to plotting.
Pygfx is expressive in what you can do with it, but does not try hard to reduce the number of code-lines. We deliberately leave higher-level (domain specific) API's to downstream libraries.


## <i class='fas'></i> Ecosystem

The following notable projects build on top of Pygfx or wgpu-py:

<div class='project-container'>

    <div class='project-container'>
        <div class=projectbox>
            <a class='button' href='http://www.fastplotlib.org/ver/dev'><i class='fas'></i> Docs</a>
            <a class='button' href='https://github.com/fastplotlib/fastplotlib'><i class='fab'></i> Source</a>
            <h3>Fastplotlib</h3>
            Next-gen plotting library built on Pygfx.
        </div>
    </div>

    <div class='project-container'>
        <div class=projectbox>
            <a class='button' href='https://github.com/pygfx/shadertoy'><i class='fab'></i> Source</a>
            <h3>Shadertoy</h3>
            Shadertoy implementation based on wgpu-py
        </div>
    </div>

</div>


<a name='sponsors' />

## <i class='fas'></i> Current sponsors

Pygfx is open source and free to use. To develop these projects we rely on funding from our sponsors. The more groups contribute, the more time we can spend on moving these projects forwards. [Learn more ...](sponsor.html)

<div class=sponsorbox>
    <h3>Ramona optics</h3>
    <img src='https://www.ramonaoptics.com/icons/icon-256x256.png' /><br>
    <a href='https://www.ramonaoptics.com/'>https://ramonaoptics.com</a>
</div>

<div class=sponsorbox>
    <h3>The Flatiron institute</h3>
    <img src='https://sf-web-assets-prod.s3.amazonaws.com/wp-content/uploads/2023/09/18102348/Simons-Foundation-Logo_blue.png' /><br>
    <a href='https://www.simonsfoundation.org/flatiron/'>https://simonsfoundation.org/flatiron/</a>
</div>



## <i class='fas'></i> Core team

<div class=profilebox>
    <img class='profile' src='https://github.com/almarklein.png' /><br>
    <a href='https://github.com/almarklein'>@almarklein</a>
</div>

<div class=profilebox>
    <img class='profile' src='https://github.com/korijn.png' /><br>
    <a href='https://github.com/korijn'>@korijn</a>
</div>


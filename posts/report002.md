# What's up for 2025

<!-- DATE: 2025-01-17 -->
<!-- AUTHOR: Almar -->

In this post I outline the plans for 2025.

<!-- END_SUMMARY -->


## Funding

With the currently accumulated funds, and current/upcoming sponsoring contracts, we
can continue well into 2025. Additional sponsorships are very welcome though, so we can
hire contractors, maybe organize an event, and build up some runway to get into 2026.


## Priorities

The overarching priority is still to move towards a "1.0 version" after
which our API can be more stable, as well as more feature-complete.


## Update propagation

We already did a lot of work on update propagation and renderer / viewport refactoring in the second part of [2024](report001.html).
We actually hoped to finish this work in 2024, but that's how things go.

These changes will introduce backwards incompatibilities in the API of
Pygfx. This means that it will cause some work and pain for downstream projects.
But it will be worth it, as it makes Pygfx more future-proof, opening up
more possibilities for new features and performance enhancements, with a cleaner API.


## Plotting features

Another big focus will be on support for plotting features, like map projections, logarithmic
ticks, axes and subplots, and more.

This will allow [Fastplotlib](https://github.com/fastplotlib/fastplotlib) to
move to a next level, and make it easier to create other high-level scientific tools with Pygfx.


## Performance

Performance optimizations continue to be an effort. Most notably to reduce
the overhead when rendering many objects. Things to think about are
multi-text objects, better caching to reduce overhead iterating over all objects,
and making use of WebGPU's render bundles.


## Remote rendering

We also have plans to improve support for remote rendering to `rendercanvas`.
This includes research to optimising performance of sending the rendered images
to another place, which will also benefit [jupyter_rfb](https://github.com/vispy/jupyter_rfb).

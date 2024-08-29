```{toctree}
:hidden: true
```

# {octicon}`terminal` Installation

The following instructions require that you have [Anaconda](https://www.anaconda.com/) installed. It is recommended to create an Anaconda virtual environment to prevent conflicting package dependencies. The package can be installed from PyPI via [pip](https://pypi.org/project/pip/) (recommended) or from the [GitHub repository](https://github.com/pkosurilab/BellaVista). Bella Vista requires python 3.9 or above.

**Create and activate a new virtual environment:**

```{eval-rst}
.. code-block:: python

    conda create -n bellavista_env python=3.9
    conda activate bellavista_env
```


**Installation via pip:**

```{eval-rst}
.. code-block:: python

    pip install bellavista
```

**Or installation from GitHub repository:**

```{eval-rst}
.. code-block:: python

    git clone https://github.com/pkosurilab/BellaVista
    pip install -e BellaVista
```

To start exploring your data in Bella Vista see [Getting Started](get_started)

If you are encountering any issues, please [open a new issue](https://github.com/pkosurilab/BellaVista/issues) in the GitHub repository. Feedback is welcome and appreciated!

<div class="flex justify-between items-center pt-6 mt-12 border-t border-border gap-4">
    <div class="mr-auto">
      <a href="index.html" class="inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors border border-input hover:bg-accent hover:text-accent-foreground py-2 px-4" style="text-decoration: none;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2 h-4 w-4">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
        Home
      </a>
    </div>
  <div class="ml-auto">
    <a href="get_started.html" class="inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors border border-input hover:bg-accent hover:text-accent-foreground py-2 px-4" style="text-decoration: none;">
      Getting Started
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="ml-2 h-4 w-4">
        <polyline points="9 18 15 12 9 6"></polyline>
      </svg>
    </a>
  </div>
</div>
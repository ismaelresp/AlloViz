<!-- [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/correlationplus)](https://pypi.org/project/correlationplus/)
[![PyPI](https://img.shields.io/pypi/v/correlationplus)](https://pypi.org/project/correlationplus/)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/correlationplus/README.html)
[![Open Source License: GPL v3](https://img.shields.io/badge/License-LGPLv3-blue.svg)](https://opensource.org/licenses/LGPL-3.0)
[![Doc](https://readthedocs.org/projects/correlationplus/badge/?version=latest)](http://correlationplus.readthedocs.org/en/latest/#)
[![Docker Image Version (tag latest semver)](https://img.shields.io/docker/v/structuraldynamicslab/correlationplus/latest)](https://hub.docker.com/repository/docker/structuraldynamicslab/correlationplus)
![Conda](https://img.shields.io/conda/pn/bioconda/correlationplus)
[![SWH](https://archive.softwareheritage.org/badge/origin/https://github.com/tekpinar/correlationplus/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/tekpinar/correlationplus) -->

# AlloViz 🔭

A Python package to interactively computate, analyze and visualize protein allosteric communication (residue interaction) networks and delta-networks.

AlloViz binds together some new modules with 6 Python packages that provide different ways of calculating residue interactions: [getcontacts](https://github.com/getcontacts/getcontacts), [correlationplus](https://github.com/tekpinar/correlationplus), [dynetan](https://github.com/melomcr/dynetan), [PyInteraph2](https://github.com/ELELAB/pyinteraph2), [pytraj](https://github.com/Amber-MD/pytraj) and [MD-TASK](https://github.com/RUBi-ZA/MD-TASK).

For the same topology and molecular dynamics (MD) trajectory, the network can be constructed based on residue contacts, movement correlation or pseudo-interaction energies, depending on the package selected. Moreover, for movement correlation, the movement tracked can be that of the whole residue, its center of mass, its alpha-C or its beta-C; and it can be calculated as the Pearson's correlation coefficient, Mutual Information (MI) or Linear MI (LMI). See [below](#available-information-sources-for-network-generation).

The network can be analyzed with edge centrality metrics algorithms provided by the Python package [networkx](https://github.com/networkx/networkx), and they can be visualized in a Notebook using [nglview](https://github.com/nglviewer/nglview).

## Installation

It is recommended to use a virtual environment. This repository includes submodules that need to be appropriately cloned alongside the main repository using the `--recursive` flag. At present, virtual environment dependencies can only be installed with conda due to vmd-python not being available in PyPi.

```bash
git clone --recursive https://github.com/frannerin/AlloViz
cd AlloViz
conda create AlloViz -c conda-forge --file environment.txt
```

Then install AlloViz preferably with `pip install .`. Alternatively, use `python setup.py install`.

## Quickstart

### for GPCRmd files

There are two main classes to be used: `State` and also `Pair`, for delta-network analysis.

A State is defined with a name and the GPCRmd dynamics ID number. For example:

```bash
activeB2AR = AlloViz.State("activeB2AR", 169)
```

And then network computations, analyses and visualizations are performed with associated methods. For example:

```bash
activeB2AR.calculate(pkg = "Getcontacts")
activeB2AR.analyze(metrics = "btw")
activeB2AR.view()
```

## Available information sources for network generation

<table style="undefined;table-layout: fixed; width: 539px">
<colgroup>
<col style="width: 195px">
<col style="width: 111px">
<col style="width: 124px">
<col style="width: 109px">
</colgroup>
<thead>
  <tr>
    <th>Residue information extracted from trajectories</th>
    <th>Package</th>
    <th>Correlation measurement</th>
    <th>Subset of atoms tracked</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Contact frequency</td>
    <td>getcontacts</td>
    <td></td>
    <td>Whole residue</td>
  </tr>
  <tr>
    <td rowspan="2">PyInteraph2</td>
    <td></td>
    <td>Whole residue</td>
  </tr>
  <tr>
    <td>Pseudo-interaction energies</td>
    <td></td>
    <td>Whole residue</td>
  </tr>
  <tr>
    <td rowspan="9">Movement correlation</td>
    <td rowspan="2">dynetan</td>
    <td rowspan="2">Mutual Information (MI)</td>
    <td>Whole residue</td>
  </tr>
  <tr>
    <td>Residue COM</td>
  </tr>
  <tr>
    <td rowspan="2">pytraj</td>
    <td rowspan="2">Pearson's</td>
    <td>alpha-C</td>
  </tr>
  <tr>
    <td>beta-C</td>
  </tr>
  <tr>
    <td>MD-TASK</td>
    <td>Pearson's</td>
    <td>alpha-C</td>
  </tr>
  <tr>
    <td rowspan="5">correlationplus</td>
    <td rowspan="2">Pearson's</td>
    <td>alpha-C</td>
  </tr>
  <tr>
    <td>Residue COM</td>
  </tr>
  <tr>
    <td rowspan="2">Linear MI</td>
    <td>alpha-C</td>
  </tr>
  <tr>
    <td>Residue COM</td>
  </tr>
  <tr>
    <td rowspan="2">Dihedral correlation</td>
    <td>Pearson's</td>
    <td>phi, psi and omega</td>
  </tr>
  <tr>
    <td>Adrián's script</td>
    <td>MI</td>
    <td>-</td>
  </tr>
</tbody>
</table>

## Cite
--

## Licensing
:upside_down_face:

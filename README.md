# validation-component-bootstrap-utils
Collection of scripts and utilities for bootstrapping validation components.

- [validation-component-bootstrap-utils](#validation-component-bootstrap-utils)
  - [Motivation](#motivation)
  - [Improvements](#improvements)
  - [Use Cases](#use-cases)
  - [Installation](#installation)
    - [Developers](#developers)
  - [Exported scripts](#exported-scripts)
  - [Contributing](#contributing)
  - [To-Do/Coming Next](#to-docoming-next)
  - [CHANGELOG](#changelog)
  - [License](#license)



## Motivation

This will help to auto-generate some amount of boilerplate code including the following:
- record.py which contains a Pydantic Record class
- validator.py which contains a non-Pydantic Validation class
- validate_files.py which will be the primary driver of the generated validation software component

## Improvements

Please see the [TODO](TODO.md) for a list of upcoming improvements.


## Use Cases

![use case diagram](use_cases.png)


## Installation

Clone this project and then run the pip installer

```bash
git clone https://github.com/jai-python3/validation-component-bootstrap-utils.git
cd validation-component-bootstrap-utils
virtualenv -p python3 venv
source venv/bin/activate
python setup.py sdist
pip install .
```

You can uninstall like this:

```bash
pip uninstall validation-component-bootstrap-utils
make clean
```

### Developers

If you modify the code in this package in your local virtual environment:

```shell
pip uninstall validation-component-bootstrap-utils
make clean
python setup.py sdist
pip install .
```

If you want to export the code in this package to the PYPI repository:

Install `twine` and `setuptools`:

```shell
pip install twine setuptools
```


Build the Distribution Package

```shell
python setup.py sdist bdist_wheel
```

Configure your ~/.pypirc:

```bash
[pypi]
  username = __token__
  password = pypi-YOUR-TOKEN
```

Upload Your Package to PyPI

```shell
twine upload dist/*
```


Now you can install your package in your Python virtual environment

```shell
pip install validation-component-bootstrap-utils
```

![class diagrams](class_diagrams.png)


## Exported scripts

To use the exported script `bootstrap-validation-component`.

For example:

```bash
bootstrap-validation-component  --infile examples/sample.tsv --data_file_type VCF --namespace su.vcf --verbose                           
--config_file was not specified and therefore was set to 
'/home/sundaram/projects/validation-component-bootstrap-utils/venv/lib/python3.10/site-packages/validation_component_bootstrap_utils/conf/conf
ig.yaml'
--outdir was not specified and therefore was set to '/tmp/generate_validation_module/2023-12-19-123510'
Created output directory '/tmp/generate_validation_module/2023-12-19-123510'
--template_path was not specified and therefore was set to 
'/home/sundaram/projects/validation-component-bootstrap-utils/venv/lib/python3.10/site-packages/validation_component_bootstrap_utils/templates
/validation'
--logfile was not specified and therefore was set to '/tmp/generate_validation_module/2023-12-19-123510/generate_validation_module.log'
Wrote validator.py file '/tmp/generate_validation_module/2023-12-19-123510/su/vcf/validator.py'
Wrote validate_file.py file '/tmp/generate_validation_module/2023-12-19-123510/validate_file.py'
Wrote column report file '/tmp/generate_validation_module/2023-12-19-123510/0_#CHROM.tsv'
Wrote column report file '/tmp/generate_validation_module/2023-12-19-123510/1_POS.tsv'
Wrote column report file '/tmp/generate_validation_module/2023-12-19-123510/2_ID.tsv'
Wrote column report file '/tmp/generate_validation_module/2023-12-19-123510/3_REF.tsv'
Wrote column report file '/tmp/generate_validation_module/2023-12-19-123510/4_ALT.tsv'
Wrote column report file '/tmp/generate_validation_module/2023-12-19-123510/5_QUAL.tsv'
Wrote column report file '/tmp/generate_validation_module/2023-12-19-123510/6_FILTER.tsv'
Wrote column report file '/tmp/generate_validation_module/2023-12-19-123510/7_INFO.tsv'
Wrote record.py file '/tmp/generate_validation_module/2023-12-19-123510/su/vcf/record.py'
The log file is '/tmp/generate_validation_module/2023-12-19-123510/generate_validation_module.log'
Execution of 
'/home/sundaram/projects/validation-component-bootstrap-utils/venv/lib/python3.10/site-packages/validation_component_bootstrap_utils/generate_
validation_module.py' completed
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## To-Do/Coming Next

Please view the listing of planned improvements [here](TODO.md).

## CHANGELOG

Please view the CHANGELOG [here](CHANGELOG.md).

## License

[GNU AFFERO GENERAL PUBLIC LICENSE](LICENSE)

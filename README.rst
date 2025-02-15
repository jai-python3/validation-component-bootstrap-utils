=================================================
Utilities for Bootstrapping Validation Components
=================================================

Utilities for Bootstrapping Validation Components


Validation Component Bootstrap Utils is a comprehensive set of Python scripts and utilities designed to streamline the process of parsing and validating tab-delimited or comma-separated files. This toolkit automates the generation of essential modules, making it easier to integrate file validation components into your projects.

Modules Generated

validator.py: This module provides a robust set of functions and classes for validating data within the specified file format. It ensures that the content adheres to defined standards, offering a solid foundation for data integrity.

parser.py: The parser module facilitates efficient extraction of data from tab-delimited or comma-separated files. It is engineered to handle various data structures and file layouts, ensuring flexibility and adaptability to diverse use cases.

record.py: The record module defines structures for organizing and representing individual records within the files. It lays the groundwork for maintaining data consistency and ease of manipulation during the parsing and validation processes.

file_validation.py: This module orchestrates the validation and parsing processes, providing a unified interface for users. It acts as the entry point for utilizing the toolkit, promoting simplicity and coherence in handling file operations.



Exported console script
-----------------------

* bootstrap-validation-component - This script is the main entry point for the Validation Component Bootstrap Utils toolkit. It generates the essential modules for parsing and validating tab-delimited or comma-separated files, streamlining the integration of validation components into your projects.

Usage:

.. code-block:: bash

    bootstrap-validation-component  --infile examples/sample.tsv --data_file_type VCF --namespace su.vcf --verbose                           
    --config_file was not specified and therefore was set to 
    '/home/sundaram/projects/validation-component-bootstrap-utils/venv/lib/python3.10/site-packages/validation_component_bootstrap_utils/conf/config.yaml'
    --outdir was not specified and therefore was set to '/tmp/generate_validation_module/2023-12-19-123510'
    Created output directory '/tmp/generate_validation_module/2023-12-19-123510'
    --template_path was not specified and therefore was set to 
    '/home/sundaram/projects/validation-component-bootstrap-utils/venv/lib/python3.10/site-packages/validation_component_bootstrap_utils/templates/validation'
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
    '/home/sundaram/projects/validation-component-bootstrap-utils/venv/lib/python3.10/site-packages/validation_component_bootstrap_utils/generate_validation_module.py' completed
```

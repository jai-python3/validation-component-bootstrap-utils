# -*- coding: utf-8 -*-
from datetime import datetime
import csv
import logging
import os
import sys


from typing import Dict

DEFAULT_VERBOSE = False


class Manager:
    """Class for managing the creation of the validation modules."""

    def __init__(self, **kwargs):
        """Constructor for Manager."""
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", None)
        self.logfile = kwargs.get("logfile", None)
        self.outdir = kwargs.get("outdir", None)
        self.verbose = kwargs.get("verbose", DEFAULT_VERBOSE)

        logging.info(
            f"Instantiated Manager in file '{os.path.abspath(__file__)}'"
        )

    def generate_validation_modules(self, infile: str) -> None:
        """Generate the validation modules for the specified file.

        Args:
            infile (str): the input tab-delimited or csv file
        Returns:
            None
        """
        logging.info(
            f"Will attempt to generate validation modules for input file '{infile}'"
        )
        extension = os.path.splitext(infile)[1]

        if extension == ".csv":
            self._generate_validation_modules_for_csv_file(infile)
        elif extension == ".tsv":
            self._generate_validation_modules_for_tsv_file(infile)
        else:
            logging.error(
                f"Support does not exist for files with extension '{extension}'"
            )
            sys.exit(1)

    def _generate_validation_modules_for_csv_file(self, infile: str) -> None:
        """Generate the validation modules for the specified .csv file.

        Args:
            infile (str): the input .csv file
        Returns:
            None
        """
        logging.error(
            f"NOT YET IMPLEMENTED - unable to process .csv file '{infile}'"
        )
        sys.exit(1)

    def _generate_validation_modules_for_tsv_file(self, infile: str) -> None:
        """Generate the validation modules for the specified .tsv file.

        Args:
            infile (str): the input .tsv file
        Returns:
            None
        """

        if not os.path.exists(infile):
            raise Exception(f"file '{infile}' does not exist")

        header_to_position_lookup = {}

        header_to_position_lookup = self._derive_column_headers_for_tsv_file(
            infile
        )
        self._process_columns_for_tsv_file(infile, header_to_position_lookup)

    def _process_columns_for_tsv_file(
        self, infile: str, header_to_position_lookup: Dict[str, int]
    ) -> None:
        """TBD."""
        for column_name, column_position in header_to_position_lookup.items():
            logging.info(
                f"Processing column name '{column_name}' at column position '{column_position}'"
            )

            uniq_val_lookup = {}
            uniq_val_ctr = 0

            with open(infile) as f:
                reader = csv.reader(f, delimiter="\t")
                row_ctr = 0
                for row in reader:
                    row_ctr += 1
                    if row_ctr == 1:
                        continue
                    else:
                        if len(row) == 0:
                            # Blank line to be skipped?
                            continue
                        # print(f"{row=}")
                        val = row[column_position]
                        if val not in uniq_val_lookup:
                            uniq_val_lookup[val] = 0
                            uniq_val_ctr += 1
                        uniq_val_lookup[val] += 1

            self._write_column_report_file(
                column_name,
                column_position,
                infile,
                uniq_val_ctr,
                uniq_val_lookup,
                row_ctr,
            )

    def _write_column_report_file(
        self,
        column_name,
        column_position,
        infile,
        uniq_val_ctr,
        uniq_val_lookup,
        row_ctr,
    ) -> None:
        """Write the report file for the column.

        Args:
            TODO
        Returns:
            None
        """
        outfile = self._derive_column_outfile(column_name, column_position)

        total_row_count = row_ctr - 1

        with open(outfile, "w") as of:
            of.write(f"## method-created: {os.path.abspath(__file__)}\n")
            of.write(
                f"## date-created: {str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))}\n"
            )
            of.write(f"## created-by: {os.environ.get('USER')}\n")
            of.write(f"## infile: {infile}\n")
            of.write(f"## logfile: {self.logfile}\n")

            of.write(f"Column name: '{column_name}'\n")
            of.write(f"Column position: '{column_position}'\n")
            of.write(f"Number of data rows: '{total_row_count}'\n")
            of.write(f"Here are the unique '{uniq_val_ctr}' values:\n")

            for val, count in uniq_val_lookup.items():
                percent = count / total_row_count * 100
                of.write(
                    f"value: '{val}'; count: {count}; percentage: {percent}\n"
                )

        logging.info(f"Wrote column report file '{outfile}'")
        if self.verbose:
            print(f"Wrote column report file '{outfile}'")

    def _derive_column_outfile(
        self, column_name: str, column_position: int
    ) -> str:
        """Derive the output file for the column-specific values.

        Args:
            column_name (str): the column name
        Returns:
            str: the output file
        """
        basename = (
            column_name.replace(" ", "")
            .replace("*", "")
            .replace("\\", "")
            .replace("/", "_")
            .replace("|", "_")
            .replace("(", "_")
            .replace(")", "_")
        )
        outfile = os.path.join(
            self.outdir, f"{column_position}_{basename}.tsv"
        )
        return outfile

    def _derive_column_headers_for_tsv_file(
        self, infile: str
    ) -> Dict[str, int]:
        """Derive the column headers for the input .tsv file.

        Args:
            infile (str): the file to be parsed
        Returns:
            dict: column header is the key and column number is the value
        """
        lookup = {}
        column_ctr = 0

        with open(infile) as f:
            reader = csv.reader(f, delimiter="\t")
            row_ctr = 0
            for row in reader:
                row_ctr += 1
                if row_ctr == 1:
                    for field in row:
                        lookup[field] = column_ctr
                        column_ctr += 1
                    logging.info(
                        f"Processed the header of .tsv file '{infile}'"
                    )
                    break
        logging.info(f"Found '{column_ctr}' columns in file '{infile}'")
        return lookup

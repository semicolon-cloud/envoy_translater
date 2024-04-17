from django.core.management.base import BaseCommand

import confspirator

from envoy_translator import config


class Command(BaseCommand):
    help = "Produce an example config file for envoy_translator."

    def add_arguments(self, parser):
        parser.add_argument("--output-file", default="envoy_translator.yaml")

    def handle(self, *args, **options):
        print("Generating example file to: '%s'" % options["output_file"])

        confspirator.create_example_config(config._root_config, options["output_file"])

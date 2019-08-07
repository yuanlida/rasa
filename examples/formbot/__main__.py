import os
import rasa
from rasa import version
from rasa.cli import scaffold, run, train, interactive, shell, test, visualize, data, x
from rasa.cli.arguments.default_arguments import add_logging_options
from rasa.cli.utils import parse_last_positional_argument_as_model_path
from rasa.utils.common import set_log_level
import rasa.core.visualize
import asyncio


if __name__ == "__main__":
    os.chdir('/Users/lidayuan/Documents/edison/rasa/examples/formbot')
    rasa.train(domain='domain.yml', config='config.yml', training_files='./data')
    # rasa.run(model="models", endpoints="endpoints.yml")
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(
    #     rasa.core.visualize(config_path="config.yml",
    #                         domain_path="domain.yml",
    #                         stories_path='./data/stories.md',
    #                         nlu_data_path=None,
    #                         output_path="./txt.html",
    #                         max_history=100
    #                         )
    # )



import os
import json

def set_whylogs_key(file):
    """
    This function obtains the WhyLogs key.
    """
    if "WHYLABS_API_KEY" not in os.environ or "WHYLABS_DEFAULT_ORG_ID" not in os.environ:
        try:
            f = open(file, 'r')
            json_conf=json.load(f)
            os.environ["WHYLABS_API_KEY"]=json_conf['key']
            os.environ["WHYLABS_DEFAULT_ORG_ID"]=json_conf['org']
        except FileNotFoundError:
            print('The file {} was not found.'.format(file))
            raise
        except KeyError:
            print('The file must contain keys: "key" and "org"')
            raise
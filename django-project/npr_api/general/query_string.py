"""
Query string merging.
"""

def merge_params_to_query_string(params):
    q_strings = []
    for key, value in params.iteritems():
        q_strings.append("{}={}".format(key, value))
    return "&".join(q_strings)

def merge_stem_with_query_string(stem, query_string):
    return "{}?{}".format(stem, query_string)

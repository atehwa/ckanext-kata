'''Settings and constants for Kata CKAN extension'''


# Facets used in Solr queries
# Facets need also to be changed to search.html. This all should be fixed in newer CKAN versions with IFacets interface.
FACETS = ['groups','tags','extras_fformat','license','authorstring','organizationstring','extras_language']
# Facets need also to be changed to search.html. This all should be fixed in newer CKAN versions with IFacets interface.

# Default sorting method. Pre-selects the corresponding option on search form.
DEFAULT_SORT_BY = u'metadata_modified desc'

# Titles for all fields used in searches, should be used through get_field_titles() for translation
_FIELD_TITLES = {'organizationstring': 'Organization',
                'ext_organizationstring': 'Organization',
                'tags': 'Keywords',
                'ext_tags': 'Keywords',
                'extras_fformat': 'File formats',
                'ext_extras_fformat': 'File formats',
                'groups': 'Discipline',
                'ext_groups': 'Discipline',
                'license': 'License',
                'ext_license': 'License',
                'authorstring': 'Author',
                'ext_authorstring': 'Author',
                'ext_author': 'Author',
                'extras_language': 'Language',
                'ext_extras_language': 'Language',
                'title': 'Title',
                'ext_title': 'Title',
                }

# Fields for advanced search
SEARCH_FIELDS = ['ext_organizationstring',
                'ext_tags',
                'ext_extras_fformat',
                'ext_groups',
                'ext_license',
                'ext_author',
                'ext_extras_language',
                'ext_title',
                ]


def get_field_titles(_):
    '''
    Get correctly translated titles for search fields

    :param _: gettext translator
    :return: dict of titles for fields
    '''

    translated_field_titles = {}

    for k, v in _FIELD_TITLES.iteritems():
        translated_field_titles[k] = _(v)

    return translated_field_titles

def get_field_title(key, _):
    '''
    Get correctly translated title for one search field

    :param _: gettext translator
    :return: dict of titles for fields
    '''

    return _(_FIELD_TITLES[key])
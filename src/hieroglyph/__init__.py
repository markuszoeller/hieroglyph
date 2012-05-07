import unicodedata

from hieroglyph import builder
from hieroglyph import directives
from hieroglyph import html

def setup(app):

    app.add_builder(builder.SlideBuilder)
    app.add_builder(builder.DirectorySlideBuilder)

    # core slide configuration
    app.add_config_value('slide_theme', 'slides', 'html')
    app.add_config_value('slide_levels', 3, 'html')
    app.add_config_value('slide_theme_options', {}, 'html')
    app.add_config_value('slide_theme_path', [], 'html')

    # support for linking html output to slides
    app.add_config_value('slide_link_html_to_slides', False, 'html')
    app.add_config_value('slide_link_html_sections_to_slides', False, 'html')
    app.add_config_value('slide_relative_path', '../slides/', 'html')
    app.add_config_value('slides_html_slide_link_symbol',
                         unicodedata.lookup('section sign'), 'html')

    # support for linking from slide output to html
    app.add_config_value('slide_link_to_html', False, 'html')
    app.add_config_value('slide_html_relative_path', '../html/', 'html')

    # slide-related directives
    app.add_node(directives.slides)
    app.add_directive('notslides', directives.Slides)
    app.add_directive('slides', directives.Slides)
    app.connect('doctree-resolved', directives.process_slide_nodes)

    app.connect('builder-inited', html.inspect_config)
    app.connect('html-page-context', html.add_link)

def generate_concept_HTML(concept_title, concept_description):
    html_lesson_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_lesson_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_lesson_3 = '''
    </div>
</div>'''
    
    full_html_text = html_lesson_1 + html_lesson_2 + html_lesson_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEXT = """TITLE: The Basics of the Web and HTML
DESCRIPTION: HTML means HyperText Markup Lanuage
Types of Hyperlinks are: Bold tag, Italics tag and Images tag 
TITLE: If Statements and While Loops
DESCRIPTION: If Statement is a conditional that, when it is satisfied, activates some part of code. 
While Loops is statement, which executes a block of code as long as its condition is true. The Break statement gives us a way to stop the loop while even the test condition is true.
TITLE: Structured Data 
DESCRIPTION: Structured Data is considered like a string. A string is a sequence of characters. Lists are elements that can be anything."""



def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEXT)

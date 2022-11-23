# Contact Searching

TO-DO: Make sure that you delete all of the TO-DO markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## Will Wolff

## Program Output

### What is the output from running the following commands?

```bash
- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`
```

```bash

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```bash
from contactsearcher import search
```

The source code above is asking to call the code within the file of contactsearcher and find and import the code of search and put it in the main code being used. The data needs the import in order for the output to be the desired one asked for. The imported data is used in the output by running the code for the data.

#### The source code statement that extracts the current job description for a contact
```bash

current_contact_job = contact_line[1]
        if job_description in current_contact_job.lower():
            list_contacts.append(contact_line)

```

The code is reading the current job contact and saying that equals the contactline of a 1 count. It then goes and reads that if the job description inputted is in the current contact job, then they should append that job to the list and then the list is returned and that is ouputted as a result if it is found within the list.

#### Invocation of the function called `search_for_email_given_job`

```bash

def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    list_contacts = []
    lines = csv.reader(contacts.splitlines(), delimiter=",", quotechar='"',
            quoting=csv.QUOTE_ALL, skipinitialspace=True,)
    for contact_line in lines:
        current_contact_job = contact_line[1]
        if job_description in current_contact_job.lower():
            list_contacts.append(contact_line)
    return list_contacts

```

The list contacts is first defined in the beginning same with lines as the csv reader. It is then run through a for loop looking at the current job with reads the contact line 1 spot ahead. It read an if statement asking that if the job description inputted is in the current contact job, then they should append that job to the list and then the list is returned and that is ouputted as a result if it is found within the list.

#### Test case for the function called `search_for_email_given_job`

```bash

============================= test session starts ==============================
platform darwin -- Python 3.10.6, pytest-7.1.1, pluggy-1.0.0
rootdir: /Users/willwolff/cs102/classDocs/08_survey_contact_searching-wolff01/contactsearcher
collected 5 items                                                              

tests/test_search.py .....

============================== 5 passed in 0.01s ===============================

```

This shows the result of when we run the test case in order to check for any flaws in the code htat dont give a negative results that diveret from thr expected output. When Looking at the ouputs that are expected to print with this code, this is suppoed to give us this output saying that all five of the test cases were able to pass and it was all correct.

#### Execute trace of the `contactsearcher` program

When running the command below, the output shows the full list of the requested information that was called for in the input. In the input, it is calling for the contactsearcher and inputting the words of engineer for job description and contacts.txt for contacts-file. 

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

One area I have struggled is with the print statements and what to return in my code. When trying to return code at first, I wasnt sure what was needed to print in order for the certain code to work. Most of the time when trying to run a code and I was returning something, it usually was incorrect and was giving error messages. When trying to solve what was wrong with the code, I went to Professor Bonham Carter and looked up solutions to the areas I was stuck in.

### Based on your experiences with this project, what is one way in which you want to improve?

I would try to avoid the csv reader. The csv reader seems very unnecessary and just seems like a very large loop to go around and not really needed. I think you can simplify and not use the code that was needed. The code could be changed into something using an append function or another route and it could be easier for the code to run with one less imported function.

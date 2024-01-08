<!--  Code Review Checklist

  This checklist is for PRs with a solution to a coding challenge.
  It is extra detailed to help you build good habits.

  You can delete this checklist if you are sending a PR for anything else.
  This could include: notes, planning documents, or issue templates

  Deleting this checklist doesn't mean you can be sloppy!
  You should still add a checklist appropriate to your contribution.
  Some ideas for your checklist:
  - [ ] Markdown code is correct well-formatted
  - [ ] Spelling and grammar are ok
  - [ ] ...

-->

- [ ] PR's title includes the challenge's name and language
- [ ] PR has short and clear description of the challenge
- [ ] PR has appropriate labels and milestones for easy identification
- [ ] PR it is assigned to the owner
- [ ] reviewers are assigned
- [ ] the PR contributes only one focused change
- [ ] the branch is up to date with `main`/`master`
- [ ] the code works when pulled and run locally
- [ ] all conflicts are resolved (if any)
- [ ] It is linked to an issue in the appropriate column of the project board
- [ ] feedback is addressed (if any, and if it is appropriate feedback.)

## README Documentation

- [ ] The solution is documented in `/src/README.md`
- [ ] The markdown source is formatted
- [ ] Spelling and grammar is correct in all text
- [ ] The markdown looks correct when you preview the file
- [ ] All links and images work
- [ ] The README documents the solution's behavior, strategy(ies) and implementation(s)
- [ ] There are use cases in code blocks to illustrate the function's behavior

## Python Files

- [ ] There is a module header
- [ ] There is a module docstring
- [ ] File names are in snake_case
- [ ] Test files are named `test_<module_name>.py`

## Function Docstring

- [ ] Behavior description
- [ ] Parameter description
- [ ] Return value description
- [ ] Include any assumptions
- [ ] Include 3 or more (passing!) doctests
- [ ] Include 1-2 use cases (if necessary)

## Function Implementation

- [ ] The solution is not is not copied from [djeada](https://github.com/djeada/Algorithms-And-Data-Structures)
- [ ] The code is auto-formatted
- [ ] The code has no (reasonable) linting mistakes
- [ ] Variables are named with snake_case
- [ ] The function has a clear and helpful name
- [ ] The file's name matches the function name
- [ ] The code follows the strategy as simply as possible
- [ ] Variable names are clear and helpful
- [ ] Comments explain the strategy (if necessary)
- [ ] There are type annotations
- [ ] (challenge) The code includes defensive assertions

## Unit Test Suite

- [ ] The test class has a helpful name in PascalCase
- [ ] The test class has a docstring
- Each unit test has
  - [ ] A helpful name
  - [ ] A clear docstring
  - [ ] Only one assertion
- [ ] All tests pass
- [ ] There are tests for defensive assertions
- [ ] There are tests for boundary cases
- [ ] Test suite includes black-box and glass-box tests

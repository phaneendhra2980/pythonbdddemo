Feature: Python BDD Tests with Behave Framework

    Scenario Outline: Run a Simple BDD test with Google Page
        Given I navigate to the Google page
        When I enter a searchterm
        And press enter key
        Then I should see searchresults


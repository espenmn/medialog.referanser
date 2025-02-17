# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.referanser -t test_referanse.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.referanser.testing.MEDIALOG_REFERANSER_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/medialog/referanser/tests/robot/test_referanse.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Referanse
  Given a logged-in site administrator
    and an add Referanse form
   When I type 'My Referanse' into the title field
    and I submit the form
   Then a Referanse with the title 'My Referanse' has been created

Scenario: As a site administrator I can view a Referanse
  Given a logged-in site administrator
    and a Referanse 'My Referanse'
   When I go to the Referanse view
   Then I can see the Referanse title 'My Referanse'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Referanse form
  Go To  ${PLONE_URL}/++add++Referanse

a Referanse 'My Referanse'
  Create content  type=Referanse  id=my-referanse  title=My Referanse

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Referanse view
  Go To  ${PLONE_URL}/my-referanse
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Referanse with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Referanse title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

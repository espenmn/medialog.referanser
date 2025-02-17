# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import medialog.referanser


class MedialogReferanserLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.referanser)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.referanser:default')


MEDIALOG_REFERANSER_FIXTURE = MedialogReferanserLayer()


MEDIALOG_REFERANSER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_REFERANSER_FIXTURE,),
    name='MedialogReferanserLayer:IntegrationTesting',
)


MEDIALOG_REFERANSER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_REFERANSER_FIXTURE,),
    name='MedialogReferanserLayer:FunctionalTesting',
)


MEDIALOG_REFERANSER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_REFERANSER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogReferanserLayer:AcceptanceTesting',
)

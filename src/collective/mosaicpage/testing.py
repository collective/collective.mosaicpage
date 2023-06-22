from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import zope

import collective.mosaicpage


class CollectiveMosaicpageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The autoinclude feature is disabled in the Plone fixture base layer.
        # import plone.restapi
        # self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.mosaicpage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.mosaicpage:default')


COLLECTIVE_MOSAICPAGE_FIXTURE = CollectiveMosaicpageLayer()


COLLECTIVE_MOSAICPAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_MOSAICPAGE_FIXTURE,),
    name='CollectiveMosaicpageLayer:IntegrationTesting',
)


COLLECTIVE_MOSAICPAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_MOSAICPAGE_FIXTURE,),
    name='CollectiveMosaicpageLayer:FunctionalTesting',
)

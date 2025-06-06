from krita import *

application = Krita.instance()
currentDoc = application.activeDocument()
currentLayer = currentDoc.activeNode()

noiseFilter = application.filter('unsharp')
noiseFilterConfig = noiseFilter.configuration()

noiseFilterConfig.setProperty('amount', 0)
noiseFilterConfig.setProperty('halfSize', 1.39)
noiseFilter.setConfiguration(noiseFilterConfig)

noiseFilter.apply(currentLayer, 0, 0, currentDoc.width(), currentDoc.height())
currentDoc.refreshProjection()

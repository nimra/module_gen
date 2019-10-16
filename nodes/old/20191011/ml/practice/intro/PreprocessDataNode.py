# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MinMaxScalerCode = lambda : CodeBlock(
    "",
    """
    """
)

class DataRescalingBlock(HierBlock):
    def __init__(self):
        super().__init__("Data Rescaling")
        self.add(MinMaxScalerCode())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ...(HierBlock):
    def __init__(self):
        super().__init__(...)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ...(HierBlock):
    def __init__(self):
        super().__init__(...)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ...(HierBlock):
    def __init__(self):
        super().__init__(...)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ...(HierBlock):
    def __init__(self):
        super().__init__(...)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ...(HierBlock):
    def __init__(self):
        super().__init__(...)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ...(HierBlock):
    def __init__(self):
        super().__init__(...)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PreprocessDataNode(LeafNode):
    def __init__(self):
        super().__init__("Preprocessing the Data for Model Fitting")
        self.add(DataRescalingBlock())
        self.add(StandardizationBlock())
        self.add(NormalizationBlock())
        self.add(BinarizationBlock())
        self.add(EncodingCategoricalVariablesBlock())
        self.add(InputMissingDataBlock())
        self.add(GeneratingHigherOrderPolynomialFeaturesBlock())

# eof

from . import Concept

class GlobalConcept(Concept):

    pass

    @staticmethod
    def convert_local_to_global(local_concept):
        global_concept = GlobalConcept(id=-1, first=local_concept.first, rel=local_concept.rel, second=local_concept.second)
        return global_concept
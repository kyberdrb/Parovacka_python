class Participant:

    def __init__(self, pa_name, pa_has_somebody_to_gift=False):
        self._name = pa_name
        # I don't use this property in my algorithm :P
        self._has_somebody_to_gift = pa_has_somebody_to_gift

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, pa_name):
        self._name = pa_name

    @property
    def has_somebody_to_gift(self):
        return self._has_somebody_to_gift

    @has_somebody_to_gift.setter
    def has_somebody_to_gift(self, pa_has_somebody_to_gift):
        self._has_somebody_to_gift = pa_has_somebody_to_gift

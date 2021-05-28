class Training:
    def __init__(self, name=None, instructor=None, duration=None, content=None):
        self._name = name
        self._instructor = instructor
        self._duration = duration
        self._content = content

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, setter):
        self._name = setter

    @property
    def instructor(self):
        return self._instructor

    @instructor.setter
    def instructor(self, setter):
        self._instructor = setter

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, setter):
        self._duration = setter

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, setter):
        self._content = setter

    def to_json(self):
        return {'name':self._name, \
            'instructor':self._instructor, \
            'duration':self._duration, \
            'content':self._content}

    def __repr__(self):
        return str(self.to_json())

    @classmethod
    def from_json(cls, data):
        return cls(**data)

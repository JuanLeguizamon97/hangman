class Reading:

    def __init__(self, archive):
        self.archive = archive

    def read(archive):
        data = []
        with open(archive, "r", encoding="utf-8") as f:
            for line in f:
                data.append(line)
        return(data)

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRBendaFreqCount(MRJob):
    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_benda,
                reducer=self.reducer_benda,
            )
        ]

    def mapper_benda(self, _, line):
        # WORD_RE.findall(line) output akan berbentuk list
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def reducer_benda(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
    MRBendaFreqCount.run()

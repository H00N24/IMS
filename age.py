
class Age():

    def __init__(self, age, year, prob):
        self.age = age
        self.year = year
        self.prob = prob
        self.ppl_s_h = 0
        self.ppl_s_nh = 0
        self.ppl_h = 0
        self.ppl_d = 0
        self.ppl_nh = 0
        self.d_prob = 0
        self.nh_prob = 0

    def alive(self):
        return self.ppl_h + self.ppl_nh

    def dead(self):
        return self.ppl_d

    def resolve_year(self):
        if self.ppl_s_h != 0 or self.ppl_s_nh != 0:
            self.ppl_h = 0
            self.ppl_nh = 0
            self.ppl_d = 0

            self.d_prob = self.prob.dead_prob(self.year,
                                              self.age)
            self.nh_prob = self.prob.nursing_house_prob(self.year,
                                                        self.age)

            self.ppl_d = round(self.ppl_s_h * self.d_prob, 0)
            alive = self.ppl_s_h - self.ppl_d
            self.ppl_nh = round(alive * self.nh_prob, 0)
            self.ppl_h = alive - self.ppl_nh
            self.ppl_s_h = 0

            dead = round(self.ppl_s_nh * self.d_prob)
            self.ppl_nh += self.ppl_s_nh - dead
            self.ppl_d += dead
            self.ppl_s_nh = 0

            self.year += 1

        return (self.ppl_h, self.ppl_nh)

import typing

def cumsumsum(arr: typing.List[typing.Any]) -> typing.List[typing.Any]:
    value = 0
    for i in range(len(arr)):
        value += (len(arr) - i) * arr[i]
    return value


class TipCalculator:
    dinner_times: typing.List[int]
    travel_times: typing.List[int]
    dinner_times_sum: int

    def __init__(
        self,
        dinner_times: typing.List[int],
        travel_times: typing.List[int],
    ) -> None:
        self.dinner_times = dinner_times
        self.travel_times = list(enumerate(travel_times))
        self.travel_times.sort(key=lambda pair: pair[1])
        self.dinner_times_sum = sum(dinner_times)
        self.travel_times_sum = cumsumsum([pair[1] for pair in self.travel_times])

    def get_tips(self) -> int:
        return self.dinner_times_sum - self.travel_times_sum

    def change(self, idx: int, dinner_time: int, travel_time: int) -> None:
        self.dinner_times_sum = self.dinner_times_sum - self.dinner_times[idx] + dinner_time
        self.dinner_times[idx] = dinner_time
        pred = lambda i: self.travel_times[i][0] == idx
        travel_times_idx = next(filter(pred, range(len(self.travel_times))))
        old_travel_time = self.travel_times[travel_times_idx][1]
        self.travel_times[travel_times_idx] = (idx, travel_time)
        if old_travel_time < travel_time:
            self.travel_times[travel_times_idx:] = sorted(self.travel_times[travel_times_idx:], key=lambda pair: pair[1])
        else:
            self.travel_times[:travel_times_idx + 1] = sorted(self.travel_times[:travel_times_idx + 1], key=lambda pair: pair[1])
        self.travel_times_sum = cumsumsum([pair[1] for pair in self.travel_times])

# troubles with case n = 1, q = 1
if __name__ == "__main__":
    n, q = map(int, input().split())

    dinner_times = [0] * n
    travel_times = [0] * n

    for i in range(n):
        # maybe floats?
        dinner_times[i], travel_times[i] = map(int, input().split())

    changes = [0] * q
    for i in range(q):
        # maybe floats?
        changes[i] = tuple(map(int, input().split()))

    calc = TipCalculator(dinner_times, travel_times)
    print(calc.get_tips())

    for i in range(len(changes)):
        idx, dinner_time, travel_time = changes[i]
        idx -= 1
        calc.change(idx, dinner_time, travel_time)
        print(calc.get_tips())

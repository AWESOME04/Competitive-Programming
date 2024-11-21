class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_time = defaultdict(dict)
        invalid = []

        for transaction in transactions:
            name, str_time, amnt, city = transaction.split(',')
            time = int(str_time)

            if name not in transaction_time[time]:
                transaction_time[time][name] = {city}
            else:
                transaction_time[time][name].add(city)

        for transaction in transactions:
            name, str_time, amnt, city = transaction.split(',')
            time = int(str_time)

            if int(amnt) > 1000:
                invalid.append(transaction)
                continue

            for inv_time in range(time - 60, time + 61):
                if inv_time not in transaction_time:
                    continue

                if name not in transaction_time[inv_time]:
                    continue

                trans = transaction_time[inv_time][name]

                if city not in trans or len(trans) > 1:
                    invalid.append(transaction)
                    break

        return invalid

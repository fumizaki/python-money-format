
class MoneyFormat:

    @staticmethod
    def yen(n: int):
        """
        int: 1234 -> str: '1,234'
        """
        s = str(n)
        # 結果格納用
        result = []
        # +-判別用
        sign = 1

        # 先頭がマイナスの場合
        if s[0] == '-':
            sign = -1
            s = s[1:]

        # 桁数確認用
        digit = 0

        index = 0
        while index < len(s):
            digit += 1
            # リストの最後尾から順に追加する
            result.append(s[len(s)-1-index])
            # 3桁ごとにカンマを追加する(先頭の場合は追加しない)
            if index + 1 < len(s) and digit % 3 == 0:
                result.append(',')
            index += 1

        # マイナスの場合、符号を追加する
        if sign == -1:
            result.append('-')

        return ''.join(result[::-1])


    @staticmethod
    def test():
        print('---test1---')
        input = 1234
        expected = "1,234"
        res = MoneyFormat.yen(input)
        assert expected == res, 'actual: {}, expected: {}'.format(res, expected)

        print('---test2---')
        input = -1234
        expected = "-1,234"
        res = MoneyFormat.yen(input)
        assert expected == res, 'actual: {}, expected: {}'.format(res, expected)

        print('---test3---')
        input = -123456
        expected = "-123,456"
        res = MoneyFormat.yen(input)
        assert expected == res, 'actual: {}, expected: {}'.format(res, expected)


if __name__ == '__main__':
    MoneyFormat.test()
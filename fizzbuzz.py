
def fizzbuzz(n: int) -> str:
    """いわゆるFizzBuzz問題を解きます

    引数で渡された値に対し、以下のような文字列を返します。

    - nが3の倍数のときは"Fizz"
    - nが5の倍数のときは"Buzz"
    - nが3の倍数かつ5の倍数のときは"FizzBuzz"
    - それ以外のときはnをそのまま返します。

    >>> fizzbuzz(1)
    '1'

    >>> fizzbuzz(3)
    'Fizz'

    >>> fizzbuzz(5)
    'Buzz'

    >>> fizzbuzz(15)
    'FizzBuzz'
    """
    pass


def runtest() -> bool:
    print("テストを実施します")
    import doctest
    result = doctest.testmod()
    return result.failed == 0

if __name__ == "__main__":
    if not runtest():
        print("テスト失敗")

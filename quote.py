import random

quotes = [
    ("每一位大神，都曾是初学者。", "匿名"),
    ("代码写得好不好，注释说了算。", "程序员谚语"),
    ("先让它跑起来，再让它跑得好。", "Kent Beck"),
    ("简单是可靠的先决条件。", "Edsger Dijkstra"),
    ("任何傻瓜都能写出计算机能理解的代码，好的程序员写出人能读懂的代码。", "Martin Fowler"),
    ("学习编程最好的时间是十年前，其次是现在。", "改编自谚语"),
    ("Bug 不是错误，是隐藏的功能。", "程序员幽默"),
    ("人生苦短，我用 Python。", "Python 社区"),
    ("不要重复造轮子，除非你想学习如何造轮子。", "开源精神"),
    ("每天进步一点点，一年后你会感谢今天的自己。", "匿名"),
]

def get_random_quote():
    quote, author = random.choice(quotes)
    print("\n" + "=" * 50)
    print(f"  💡 {quote}")
    print(f"                        —— {author}")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    print("🎲 随机名言生成器")
    print("每次运行都会给你一句不同的话\n")
    get_random_quote()
    print("再运行一次试试？  python quote.py")

from src.summarizer.engine import summarize_website


def main():
    print("Hello from summa-crawl!")

    url = input("Enter website URL: ")
    summarize_website(url)


if __name__ == "__main__":
    main()

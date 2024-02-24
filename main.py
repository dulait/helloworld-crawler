import time

from scraper.scraper import Scraper


class Main:
    @staticmethod
    def run():

        scraper = Scraper()
        start_time = time.time()

        try:
            scraper.scrape_pages(0, 917)
        except KeyboardInterrupt:
            print("\n❌Scraping interrupted. Exiting...")

        total_time_elapsed = time.time() - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(total_time_elapsed))
        total_milliseconds = int((total_time_elapsed - int(total_time_elapsed)) * 1000)

        print(f"\n🕒Total time elapsed: {formatted_time}.{total_milliseconds:03d} seconds")


if __name__ == "__main__":
    Main.run()

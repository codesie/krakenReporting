import json
import logging as logger

from krakenConnector import KrakenRequests


def main():
    """
    Main function of the script. Gets all trades and consolidates the data.

    logger (logging): logging handler for writing to the log file
    """
    config_file = "/mnt/linuxData/01_Joel/02_Freizeit/Kryptowährungen/krakenReporting/config.json"

    # initialize krakenConnector
    krqsts = KrakenRequests(config_file)

    # 2 - Create order
    result_offset = 0
    json_file = open("logs/trades.json", "a")
    final_result = {}
    # sum = 0
    new_results = True

    while new_results:
        logger.info("-- Get trade history with offset: " + str(result_offset))
        # query the trading history from the api
        data = {"ofs": result_offset}
        result = krqsts.get_trades(data)

        if 50 == len(result["result"]["trades"]):
            result_offset += 50
        else:
            new_results = False
        # new_results = False

        final_result.update(result["result"]["trades"])

        # logger.debug(result)

    json.dump(final_result, json_file)


if __name__ == "__main__":
    """
    Main entry of the script. First, the provided arguments are parsed and then the main purpose of the script is 
    executed.
    """
    main()

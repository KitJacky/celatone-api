import func.constants as constants
import func.helper as helper


def get_balances(app, chain, network, account_address):
    output_balances = []
    match chain:
        case "osmosis":
            app.logger.info("PATH: " + f"{chain} + {network}")
            app.logger.info("PATH: " + f"{constants.LCD_DICT[chain][network]}")
            output_balances = helper.get_native_balances(
                app,
                f"{constants.LCD_DICT[chain][network]}",
                chain,
                network,
                account_address,
            )
        case "terra2":
            output_balances = helper.get_native_balances(
                f"{constants.LCD_DICT[chain][network]}",
                chain,
                network,
                account_address,
            ) + helper.get_hive_balance(chain, network, account_address)
    return output_balances

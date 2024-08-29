from Scraping.scraping import *

try:
    with Scraping() as bot:
        bot.land_first_page()
        state_list = bot.state_info()
        for state in state_list:
            bot.select_state(state.strip())
            district_list = bot.district_info()
            for district in district_list:
                bot.select_district(district.strip())
                sub_district_list = bot.sub_district_info()
                for sub_district in sub_district_list:
                    bot.select_sub_district(sub_district.strip())
                    block_list = bot.block_info()
                    for block in block_list:
                        bot.select_block(block.strip())
                        village_list = bot.village_info()
                        count = 1
                        for village in village_list:
                            bot.select_village(village.strip())
                            bot.click_search(state,district,sub_district,block,village)
                            if count == 2:
                                exit(0)
        bot.final_result()


except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise

====================== =========================================
Settings                  Value
====================== =========================================
Library                 ${EXECDIR}/selenium_scripts/email.py
Force Tags		        tags.selenium
====================== =========================================

================================================================================================= ================================ ================================================================= ============================ ===================================
Test Case                                                                                           Action                           Argument                                                        Argument                       Argument     
================================================================================================= ================================ ================================================================= ============================ ===================================
DXUITC-351:To check if proper email id is getting accepted                                          test_351                        ${EXECDIR}/rate_cards/rate_card_USD.xls
DXUITC-354: To check if invalid email id is not getting accepted                                    test_354                        ${EXECDIR}/rate_cards/rate_card_USD.xls
DXUITC-437: check if new agency group is not created when more than 255 characters are entered      test_437                        ${EXECDIR}/rate_cards/rate_card_USD.xls
DXUITC-455:To check for invalid email id(@dataxu.com)                                               test_455                        ${EXECDIR}/rate_cards/rate_card_USD.xls
DXUITC-457:To check for invalid email id(test@) not acepted                                         test_457                        ${EXECDIR}/rate_cards/rate_card_USD.xls
DXUITC-1297:To check if htmal tags are not accepted                                                 test_1297                       ${EXECDIR}/rate_cards/rate_card_USD.xls
DXUITC-355:To check if new agency group is created with blank email id field                        test_355                        ${EXECDIR}/rate_cards/rate_card_USD.xls
DXUITC-436: To check if new agency group is created with 255 characters in email id field           test_436                        ${EXECDIR}/rate_cards/rate_card_USD.xls
================================================================================================= ================================ ================================================================= ============================ ===================================
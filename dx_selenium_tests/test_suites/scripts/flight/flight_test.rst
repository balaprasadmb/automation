================= ========================
Settings           Value
================= ========================
Library            flight_test.FlightTest
Force Tags         flights
================= ========================


===================================================================================== =================================================== ==========================
 Test Case                                                                             Action                                              Argument
===================================================================================== =================================================== ==========================
DXUITC-6504:Flight should not created with blank name                                   Login As Campaign Manager
\                                                                                       Blank Message Validation
\                                                                                       Verify Blank Flight Name
DXUITC-2495:To check if flight is created when Budget is kept blank                     Verify Blank Bid Name
DXUITC-2479:To check if flight is created when bid is kept blank                        Verify Blank Budget Name
DXUITC-2482:To check if flight is created when negative numbers are entered             Fill Fields With Negative Values
\                                                                                       Verify Negative Bid
DXUITC-2498:To check if flight is created when negative numbers are entered             [Tags]                                             non-critical
\                                                                                       Verify Negative Budget
DXUITC-2375:To verify Frequency cap not accepts alphanumeric values                     Fill Fields With Alphanumeric Values
\                                                                                       Verify Alphanumeric Values For Frequency Cap
DXUITC-2440:To verify Impression cap not accepts alphanumeric values                    Verify Alphanumeric Values For Impression Cap
DXUITC-2376:To verify Frequency cap as optional                                         Valid Flight Flow
\                                                                                       Create Flight With Valid Data
DXUITC-2438:To verify Impressions cap as optional                                       Create Flight With Valid Data
DXUITC-1856:To check if flight is created when less than 100 characters are filled      Create Flight With Valid Data
DXUITC-1861:To check if flight is created when special characters are entered           Create Flight With Valid Data
DXUITC-1857:To check if flight is created when 100 or less than 100 characters          Create Flight With Valid Data
DXUITC-1867:To check if flight is created when numbers are entered                      Create Flight With Valid Data
DXUITC-1868:To check if flight is created when alphanumeric characters are entered      Create Flight With Valid Data
DXUITC-2509:To check if flight is created when valid data is entered                    Create Flight With Valid Data
DXUITC-2499:To check if flight is created when decimal number is entered                Create Flight With Valid Data
DXUITC-2483:To check if flight is created when decimal number is entered                Create Flight With Valid Data
DXUITC-2480:To check if flight is created when valid data is entered                    Create Flight With Valid Data
DXUITC-2491:To check if flight is created when decimal number is entered                Create Flight With Valid Data
DXUITC-2507:To check if flight is created when valid data is entered                    Create Flight With Valid Data
DXUITC-2450:To check working of "save and continue" button                              Create Flight With Valid Data
DXUITC-1890:To check if valid start date can be put manually                            Create Flight With Valid Data
DXUITC-1893:To check if characters can be put in start date field manually              Create Flight With Valid Data
DXUITC-1898:To check if special characters can be put in start date field manually      Create Flight With Valid Data
DXUITC-1891:To check if valid end date can be put manually                              Create Flight With Valid Data
DXUITC-1895:To check if characters can be put in end date field manually                Create Flight With Valid Data
DXUITC-1897:To check if special characters can be put in end date field manually        Create Flight With Valid Data
DXUITC-1533:To verify Campaign Start Date accepts date in future                        Create Flight With Valid Data
DXUITC-1874:To check working of start date calendar                                     Create Flight With Valid Data
DXUITC-2442:To check proper values for Impression cap                                   Create Flight With Valid Data
DXUITC-1888:TO check Contents of 'Flight Budget & Schedule Set up' page                 To Check FBS Content
DXUITC-1777:To check working of master-checkbox(at the bottom)                          To Check Master Checkbox
DXUITC-1783:To check working of "filter by description" search box invalid data         To Check Description Filter Functionality
DXUITC-1848:To check working of "filter by tactic" drop down                            To Check Tactic Filter Functionality
DXUITC-2452:To check working of "add flight" button                                     To Check Add Flight Functionality
DXUITC-2449:To check working of "save and exit" button                                  To Check Save And Exit Button Functionality
DXUITC-3401:To check different flights can be created under online campaign             Online Campaign With Multiple Flights
DXUITC-340:To check if different flights can be created under mobile campaign           Mobile Campaign With Multiple Flights
DXUITC-3403:To check if different flights can be created under video campaign           Video Campaign With Multiple Flights
DXUITC-3066:To check if description can be edited with numerical characters             Edit Flight Description Validation
\                                                                                       Success Edit Flight Creation
DXUITC-3067:To check if description can be edited with special characters               Success Edit Flight Creation
DXUITC-3069:To check if description can be edited with upper case characters            Success Edit Flight Creation
DXUITC-3061:To check description edited with less than 255 characters                   Verify Long Flight Name Validation
\                                                                                       Success Edit Flight Creation
DXUITC-3063:To check if description can be edited with 100 characters                   Success Edit Flight Creation
DXUITC-3064:To check if description can be edited with more than 255 characters         Success Edit Flight Creation
DXUITC-3406:To check working of save and continue button                                Success Edit Flight Creation
DXUITC-3080:To check if flight is created when start date field is kept blank           Validation For Blank Scenarios
\                                                                                       Start Date Blank Message
DXUITC-3086:To check if flight is created when end date field is kept blank             [Tags]                                             non-critical
\                                                                                       End Date Blank Message
DXUITC-84:Add On Cost Inheritance from Parent Organization & Campaign                   Fill Campaign Details For Inheritance
\                                                                                       Verify Inherited Add On Cost
DXUITC-1497:To verify targeted languages inherited from Campaign                        Verify Inherited Lang Target
DXUITC-1501:To verify Geographic Targeting inherited from Campaign                      Verify Inherited Geo Target
DXUITC-1522:To verify no targeted languages inherited from Campaign                     Verify Lang Target Not Inherited
DXUITC-1524:To verify Geographic Targeting not inherited from Campaign                  Verify Geo Target Not Inherited
DXUITC-1773:To check working of mastercheckbox                                          Working Of Master Checkbox
DXUITC-2453:To check working of check box for flights                                   Working Of Flights Checkbox
DXUITC-6242:Flight gets created with start date and end date as empty                   Flights Created With Blank Dates
DXUITC-3280:Spent text box                                                              Spent Should Disabled
DXUITC-3355:deals section is available to users having permission of deals              Verify Deals Section Available
DXUITC-3352:To check contents of flight deals section                                   Verify Contents Of Deals
DXUITC-3361:To check working of search box for invalid data                             Search For Invalid Data
DXUITC-3363:To check working of search box for valid data                               Search For Valid Data
DXUITC-3362:To check working of search box when it is kept blank                        [Tags]                                             non-critical
\                                                                                       Search For Blank Data
DXUITC-3371:To check if individual checkboxes can be selected                           Working Of Checkbox
DXUITC-3421:To check if list of private inventory is visible                            Verify Content Of Private Inventory
DXUITC-3422:To check if checkboxes are working                                          Working Of Checkbox In Inventory
DXUITC-3428:Contents of Blacklist for Flight Detailed page                              Verify Content Of Blacklist
DXUITC-3502:Contents of Whitelist for Flight Detailed page                              Verify Content Of Whitelist
DXUITC-3070:To check working of fight tactic drop down                                  Working Of Tactic
DXUITC-6507:To verify "Here" link functionality on Inventory section tool tip text      Inventory Section On Flight Page
DXUITC-3334:To check Contents of Audience section                                       Verify Contents Of Audience Targeting
DXUITC-3269: Campaign Flight Budget Setup link functionality                            Working Of Link
DXUITC-6509-DXUITC-6510-DXUITC-6511-DXUITC-6512:working of buttons in Inventory         [Tags]                                             non-critical
\                                                                                       Working Of Buttons In Inventory Section
DXUITC-4591:Online Exchange Campaign as Campaign Manager                                Get Online Campaign With Exchange Media
DXUITC-4592:Mobile Exchange Campaign as Campaign Manager                                Get Mobile Campaign With Exchange Media
DXUITC-4593:Video Exchange Campaign as Campaign Manager                                 Get Video Campaign With Exchange Media
DXUITC-327:HACK-2697-Enable users select "one ad per page"                              Verify One Ad Per Page
DXUITC-4524:MoPub exchange should be visible for mobile video flights                   Verify Mopub Exchange
===================================================================================== =================================================== ==========================

import React from 'react'
import { IconButton, Box, ButtonGroup } from '@chakra-ui/react'
import { FaParking, FaRestroom } from 'react-icons/fa'
import { AiOutlineWifi } from 'react-icons/ai'
import { MdOutlineChairAlt, MdWaterDrop } from 'react-icons/md'


export const Filters = (props) => {
    const { waterOn, wifiOn, benchOn, parkingOn, toiletOn, 
        setWaterOn, setWifiOn, setBenchOn, setParkingOn, setToiletOn } = props;

    return (
        <div>
            <Box padding={4}>
                <ButtonGroup>

                    {/* Toilets */}
                    <IconButton
                        // colorScheme='cyan'
                        colorScheme='green'
                        aria-label='Search For Bathrooms'
                        icon={<FaRestroom />}
                        isActive={!toiletOn}
                        onClick={() => setToiletOn(!toiletOn)}
                    />

                    {/* Water */}
                    <IconButton
                        // colorScheme='blue'
                        colorScheme='green'
                        aria-label='Search For Water'
                        icon={<MdWaterDrop />}
                        isActive={!waterOn}
                        onClick={() => setWaterOn(!waterOn)}
                    />

                    {/* Parking */}
                    <IconButton
                        // colorScheme='gray'
                        colorScheme='green'
                        aria-label='Search For Parking'
                        icon={<FaParking />}
                        isActive={!parkingOn}
                        onClick={() => setParkingOn(!parkingOn)}
                    />

                    {/* Benches */}
                    <IconButton
                        colorScheme='green'
                        aria-label='Search for Benches'
                        icon={<MdOutlineChairAlt />}
                        isActive={!benchOn}
                        onClick={() => setBenchOn(!benchOn)}
                    />

                    {/* Wifi */}
                    <IconButton
                        // colorScheme='blackAlpha'
                        colorScheme='green'
                        aria-label='Search for Wifi'
                        icon={<AiOutlineWifi />}
                        isActive={!wifiOn}
                        onClick={() => setWifiOn(!wifiOn)}
                    />
                </ButtonGroup>
            </Box>
        </div>



    )
}
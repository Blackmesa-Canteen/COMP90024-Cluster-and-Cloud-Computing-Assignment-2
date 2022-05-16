import React, { useContext, useState } from "react";

import CheckBox from "../check-box/check-box";
import Box from "@mui/material/Box";
import { DataDisplayContext } from "../../App";
import Stack from "@mui/material/Stack";
import { Button,  Step, StepContent, StepLabel, Typography } from "@mui/material";
import LooksTwoIcon from '@mui/icons-material/LooksTwo';
import Looks3Icon from '@mui/icons-material/Looks3';
import DropdownSelector from "../dropdown-selector/dropdown-selector";
import { House_Price_Panel_Options } from "../../meta-data";

const HousePriceOptionsPanel = () => {
  const { setDisplayOptions } = useContext(DataDisplayContext)

  const [houseType, setHouseType] = useState(House_Price_Panel_Options.HOUSE_TYPE[0])
  const [priceType, setPriceType] = useState(House_Price_Panel_Options.PRICE_TYPE[0])

  const handleSubmit = () => {
    setDisplayOptions({
      houseType,
      priceType
    })
  }

  return (
    <>
      <Step key={2}>
        <StepLabel>
          <Stack direction='row' spacing={2}>
            <LooksTwoIcon sx = {{color:"#2196f3"}} />
            <Typography variant='body1' sx={{ fontWeight: '600' }}>
              Options
            </Typography>
          </Stack>
        </StepLabel>
        <StepContent>
          <Stack direction='column' spacing={2} sx={{padding: '20px'}}>
            <Stack>
              <DropdownSelector 
                menuItems={House_Price_Panel_Options.HOUSE_TYPE}
                updateWhenSelect={(houseType: string) => {
                  setHouseType(houseType)
                }}
                selectedItem={houseType}
              />
            </Stack>
            <Stack>
              <DropdownSelector 
                menuItems={House_Price_Panel_Options.PRICE_TYPE}
                updateWhenSelect={(priceType: string) => {
                  setPriceType(priceType)
                }}
                selectedItem={priceType}
              />
            </Stack>
          </Stack>
        </StepContent>
      </Step>
      <Step key={3}>
        <StepLabel>
          <Stack direction='row' spacing={2}>
            <Looks3Icon sx = {{color:"#2196f3"}} />
            <Typography variant='body1' sx={{ fontWeight: '600' }}>
              LoadData
            </Typography>
          </Stack>
        </StepLabel>
        <StepContent>
          <Box sx={{ width: '100%', height: '100%', display: 'flex', padding: '20px', alignItems: 'center' }}>
            <Button variant="contained" onClick={handleSubmit}>
              Confirm
            </Button>
          </Box>
        </StepContent>
      </Step>
    </>
  )
}

export default HousePriceOptionsPanel
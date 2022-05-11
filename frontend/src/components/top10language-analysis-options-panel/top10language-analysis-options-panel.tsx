import React from "react";

import Box from "@mui/material/Box";
import { DataDisplayContext } from "../../App";
import Stack from "@mui/material/Stack";
import { Button,  Step, StepContent, StepLabel, Typography } from "@mui/material";
import LooksTwoIcon from '@mui/icons-material/LooksTwo';
import Looks3Icon from '@mui/icons-material/Looks3';
import SliderComponent from "../slider/slider";

const Top10LanguageAnalysisOptionsPanel = () => {
  return (
    <>
      <Step key={2}>
        <StepLabel>
          <Stack direction='row' spacing={2}>
            <LooksTwoIcon sx = {{color:"#2196f3"}} />
            <Typography variant='body1' sx={{ fontWeight: '600' }}>
              Choose the time range
            </Typography>
          </Stack>
        </StepLabel>
        <StepContent>
          <Box sx={{padding: '20px'}}>
            <SliderComponent/>
          </Box>
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
            <Button variant="contained" >
              Confirm
            </Button>
          </Box>
        </StepContent>
      </Step>
    </>
  )
}

export default Top10LanguageAnalysisOptionsPanel
import React, { useContext } from "react";
import { DataDisplayContext } from "../../App";
import Stack from "@mui/material/Stack";
import Step from "@mui/material/Step";
import StepContent from "@mui/material/StepContent";
import StepLabel from "@mui/material/StepLabel";
import Typography from "@mui/material/Typography";
import LooksTwoIcon from '@mui/icons-material/LooksTwo';
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";

const TwitterAnalysisOptionPanel = () => {
  const { setOpenOptionsDrawer } = useContext(DataDisplayContext)


  return (
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
          <Box sx={{ width: '100%', height: '100%', display: 'flex', padding: '20px', alignItems: 'center' }}>
            <Button variant="contained" onClick={() => {setOpenOptionsDrawer(false)}}>
              Finish
            </Button>
          </Box>
        </StepContent>
      </Step>
    )
}

export default TwitterAnalysisOptionPanel
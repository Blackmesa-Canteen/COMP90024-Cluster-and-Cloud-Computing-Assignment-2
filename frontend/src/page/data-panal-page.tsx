import Container from "@mui/material/Container";
import React, { useContext, useMemo } from "react";
import { DataDisplayContext } from "../App";
import LeftDrawer from "../components/left-drawer/left-drawer";
import PopulationAnalysisPanel from "../components/population-analysis-panel/population-analysis-panel";
import { Scenarios } from "../meta-data";

const DataPanelPage = () => {
  const { selectedScenario } = useContext(DataDisplayContext)
  const dataPanel = useMemo(() => {
    switch(selectedScenario) {
      case Scenarios.POPULATION_ANALYSIS:
        return <PopulationAnalysisPanel/>
    }
  }, [selectedScenario])
  

  return (
    <div>
      <LeftDrawer/>
      <Container sx={{ minWidth: '100%', minHeight: '80vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }} disableGutters>
        { dataPanel }
      </Container>
    </div>
  )
}

export default DataPanelPage
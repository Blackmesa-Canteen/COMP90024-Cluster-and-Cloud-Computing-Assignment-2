import Container from "@mui/material/Container";
import React, { useContext, useEffect, useMemo, useState } from "react";
import { DataDisplayContext } from "../App";
import HousePriceAnalysisPanel from "../components/house-price-analysis-panel/house-price-analysis-panel";
import LeftDrawer from "../components/left-drawer/left-drawer";
import LockdownInfluenceAnalysisPanel from "../components/lockdown-influence-analysis-panel/lockdown-influence-analysis-panel";
import PopulationAnalysisPanel from "../components/population-analysis-panel/population-analysis-panel";
import Top10LanguageAnalysisPanel from "../components/top10language-analysis-panel/top10language-analysis-panel";
import TwitterAnalysisOptionPanel from "../components/twitter-analysis-panel/twitter-analysis-panel";
import { Scenarios } from "../meta-data";
import { fetchLanguagesCountData } from "../services/services";

const DataPanelPage = () => {
  const { setDisplayOptions, selectedScenario } = useContext(DataDisplayContext)
  const [languageCountData, setLanguageCountData] = useState<any[]>([])
  const dataPanel = useMemo(() => {
    switch(selectedScenario) {
      case Scenarios.POPULATION_ANALYSIS:
        return <PopulationAnalysisPanel/>
      case Scenarios.TOP_10_LANGUAGE_ANALYSIS:
        return <Top10LanguageAnalysisPanel languageCountData={languageCountData}/>
      case Scenarios.LOCK_DOWN_INFLUENCE_ANALYSIS:
        return <LockdownInfluenceAnalysisPanel/>
      case Scenarios.HOUSE_PRICE_ANALYSIS:
        return <HousePriceAnalysisPanel/>
      case Scenarios.TWITTER_ANALYSIS:
        return <TwitterAnalysisOptionPanel/>
    }
  }, [selectedScenario])
  
  useEffect(() => {
    if(selectedScenario === Scenarios.TOP_10_LANGUAGE_ANALYSIS) {
      fetchLanguagesCountData()
      .then(JSONData => {
        // console.log('aa')
        // console.log(Object.entries(JSONData).map(keyVale => ({
        //   date: parseFloat(parseFloat(keyVale[0].split('-').join('.')).toFixed(2)),
        //   languageCount: keyVale[1],
        // })))
        setLanguageCountData(Object.entries(JSONData).map(keyVale => ({
          date: parseFloat(parseFloat(keyVale[0].split('-').join('.')).toFixed(2)),
          languageCount: keyVale[1],
        })))
      })
    }
  }, [selectedScenario])

  useEffect(() => {
    if(languageCountData.length >= 2) {
      console.log(languageCountData)
      setDisplayOptions([languageCountData[0].date, languageCountData[languageCountData.length - 1].date])
    }
    else {
      setDisplayOptions([1,2])
    }
  }, [languageCountData])

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
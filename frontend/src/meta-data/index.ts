export enum Panels{
  POPULATION_PANEL,
}

export enum Scenarios {
  POPULATION_ANALYSIS = 'Population Analysis',
  TOP_10_LANGUAGE_ANALYSIS = 'Top 10 Languages Analysis',
  HOUSE_PRICE_ANALYSIS = 'House Price Analysis',
  LOCK_DOWN_INFLUENCE_ANALYSIS = 'Lock down influence analysis',

}

export enum Population_Panel_Options {
  TOTAL_POPULATION = 'total_population', 
  MIGRATION_POPULATION = 'migration_population', 
  NEW_MIGRATION = 'new_migration', 
  NEW_BIRTH = 'new_birth'
}

export const House_Price_Panel_Options = {
  HOUSE_TYPE: ['House', 'Unit'],
  PRICE_TYPE: ['avg', 'max']
}
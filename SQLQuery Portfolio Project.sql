select * 
from PortfolioProject..CovidDeaths
where continent is not null
order by 3,4

--select * from PortfolioProject..CovidVaccinations
--order by 3,4

--Select Data that we are going to be using

Select location, date, total_cases, new_cases, total_deaths, population
from PortfolioProject..CovidDeaths
where continent is not null
order by 1,2

--Looking at Total Cases VS Total Deaths
--Likelihood of dying if you contract covid in your country
Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
from PortfolioProject..CovidDeaths
where location like '%states%'
where continent is not null
order by 1,2

--Looking at the Total Cases VS Population in the United States

Select location, date, total_cases, population, (total_cases/population)*100 as Population_getting_Covid
from PortfolioProject..CovidDeaths
where location like '%states%'
where continent is not null
order by 1,2

--Highest infection rated countries
Select location, MAX(total_cases) as Highest_Infection_Count, population, (MAX(total_cases)/population)*100 as Percent_Population_Infected
from PortfolioProject..CovidDeaths
where continent is not null
group by population, location
order by Percent_Population_Infected DESC

--Lowest infection rated countries
Select location, MIN(total_cases) as Highest_Infection_Count, population, (MIN(total_cases)/population)*100 as Percent_Population_Infected
from PortfolioProject..CovidDeaths
where continent is not null
group by population, location
order by Percent_Population_Infected DESC

--Countries with the Highest Death Count per Population
Select location, MAX(cast(total_deaths as int)) as TotalDeaths
from PortfolioProject..CovidDeaths
where continent is not null
group by location
order by TotalDeaths DESC

--Breaking down by Continent

--Showing continents with the highest death count per population.
Select continent, MAX(cast(total_deaths as int)) as TotalDeaths
from PortfolioProject..CovidDeaths
where continent is not null
group by continent
order by TotalDeaths DESC

--GLOBAL NUMBERS

--Cases globably by date
select date, SUM(new_cases) as Cases_By_Date
FROM PortfolioProject..CovidDeaths
where continent is not null
group by date
order by 1,2

--Cases globably with total cases, total deaths as the death percentages by the date.
select date, SUM(new_cases) as TotalCases, SUM(cast(new_deaths as int)) as TotalDeaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
FROM PortfolioProject..CovidDeaths
where continent is not null
group by date
order by 1,2

--Cases globaly with total cases, total deaths as the death percentages.
select SUM(new_cases) as TotalCases, SUM(cast(new_deaths as int)) as TotalDeaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
FROM PortfolioProject..CovidDeaths
where continent is not null
order by 1,2


--Looking at Total Population vs Vaccinations

Select Death.continent, Death.location, Death.Date, Death.population, Vac.new_vaccinations, SUM(CONVERT(bigint, Vac.new_vaccinations)) OVER (Partition by death.location order by Death.location, Death.date) 
as RollingPeopleVaccinated,
From PortfolioProject..CovidDeaths Death
JOIN PortfolioProject..CovidVaccinations Vac
	ON Death.location = Vac.location
	and death.date = Vac.date
WHERE Death.continent is not null
order by 2,3


--USE CTE

With PopVsVac (continent, location, date, population, new_vaccinations, RollingPeopleVaccinated)
as 
(
Select Death.continent, Death.location, Death.Date, Death.population, Vac.new_vaccinations, SUM(CONVERT(bigint, Vac.new_vaccinations)) OVER (Partition by death.location order by Death.location, Death.date) 
as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CovidDeaths Death
JOIN PortfolioProject..CovidVaccinations Vac
	ON Death.location = Vac.location
	and death.date = Vac.date
WHERE Death.continent is not null
--order by 2,3
) 
select *, (RollingPeopleVaccinated/population)*100
from PopVsVac

--Temp Table

Create Table #PercentPopulationVaccinated (
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_Vaccinations numeric, 
RollingPeopleVaccinated numeric )

Insert into #PercentPopulationVaccinated
Select Death.continent, Death.location, Death.Date, Death.population, Vac.new_vaccinations, SUM(CONVERT(bigint, Vac.new_vaccinations)) OVER (Partition by death.location order by Death.location, Death.date) 
as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CovidDeaths Death
JOIN PortfolioProject..CovidVaccinations Vac
	ON Death.location = Vac.location
	and death.date = Vac.date
WHERE Death.continent is not null
--order by 2,3

select *, (RollingPeopleVaccinated/population)*100
from #PercentPopulationVaccinated


--CREATE VIEWS TO UTILIZE LATER FOR VISUALIZATIONS

--Percent of the Population Vaccinated
CREATE VIEW PercentPopulationVaccinated as

Select Death.continent, Death.location, Death.Date, Death.population, Vac.new_vaccinations, SUM(CONVERT(bigint, Vac.new_vaccinations)) OVER (Partition by death.location order by Death.location, Death.date) 
as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CovidDeaths Death
JOIN PortfolioProject..CovidVaccinations Vac
	ON Death.location = Vac.location
	and death.date = Vac.date
WHERE Death.continent is not null
--order by 2,3

select *
from PercentPopulationVaccinated


-- Highest Death Count per Country
Create View HighestDeathCount as

Select location, MAX(cast(total_deaths as int)) as TotalDeaths
from PortfolioProject..CovidDeaths
where continent is not null
group by location
--order by TotalDeaths DESC

Select *
From HighestDeathCount
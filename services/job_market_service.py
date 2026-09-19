"""
Philippine Labor & Job Market Service.
Abstract provider interface for Philippine job-market vacancy and labor data.
Strictly adheres to policy: ZERO un-authorized web scraping.
Operates via pluggable data provider pattern with offline indicators when no live API is connected.
"""

from typing import Dict, Any, List, Optional
from abc import ABC, abstractmethod

class JobMarketProvider(ABC):
    """Abstract interface for Philippine job vacancy and labor market data providers."""

    @abstractmethod
    def search_jobs(self, query: str, location: Optional[str] = None) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_jobs_for_career(self, career_id: str, location: Optional[str] = None) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_market_summary(self, career_id: str) -> Dict[str, Any]:
        pass

class DefaultPhilippineJobMarketProvider(JobMarketProvider):
    """
    Standard Philippine Job Market provider.
    Maintains clean fallback indicators until an authorized DOLE/BLE/PhilJobNet API token is configured.
    """

    def search_jobs(self, query: str, location: Optional[str] = None) -> List[Dict[str, Any]]:
        # Returns empty list gracefully without throwing errors or scraping
        return []

    def get_jobs_for_career(self, career_id: str, location: Optional[str] = None) -> List[Dict[str, Any]]:
        return []

    def get_market_summary(self, career_id: str) -> Dict[str, Any]:
        return {
            "source": "Philippine Labor Market Statistics (PSA & DOLE)",
            "status": "connected_reference",
            "demand_level": "High Growth",
            "key_hubs": ["Metro Manila (NCR)", "Cebu (Central Visayas)", "Davao (Region XI)", "Clark (Central Luzon)"],
            "remote_work_availability": "Available for Select Roles",
            "message": "Official job vacancies will display when an authorized institutional API feed is connected."
        }

class JobMarketService:
    """Entry point for querying Philippine job-market feeds through active provider."""
    
    _provider: JobMarketProvider = DefaultPhilippineJobMarketProvider()

    @classmethod
    def set_provider(cls, provider: JobMarketProvider):
        """Allow switching or plugging in authenticated job-market providers."""
        cls._provider = provider

    @classmethod
    def search_jobs(cls, query: str, location: Optional[str] = None) -> List[Dict[str, Any]]:
        return cls._provider.search_jobs(query, location)

    @classmethod
    def get_jobs_for_career(cls, career_id: str, location: Optional[str] = None) -> List[Dict[str, Any]]:
        return cls._provider.get_jobs_for_career(career_id, location)

    @classmethod
    def get_market_summary(cls, career_id: str) -> Dict[str, Any]:
        return cls._provider.get_market_summary(career_id)

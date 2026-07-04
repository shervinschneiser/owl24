import time

import httpx


class HTTPMonitorChecker:
    def check(
        self,
        url: str,
        timeout: int,
    ) -> dict:
        start = time.perf_counter()

        try:
            with httpx.Client(
                timeout=timeout,
                follow_redirects=True,
            ) as client:
                response = client.get(url)

            elapsed = round(
                (time.perf_counter() - start) * 1000,
                2,
            )

            return {
                "success": True,
                "status_code": response.status_code,
                "response_time": elapsed,
            }

        except httpx.HTTPError:
            elapsed = round(
                (time.perf_counter() - start) * 1000,
                2,
            )

            return {
                "success": False,
                "status_code": None,
                "response_time": elapsed,
            }

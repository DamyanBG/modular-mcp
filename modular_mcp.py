from mcp.server.fastmcp.server import FastMCP

from bundle import Bundle


class ModularFastMCP(FastMCP):
    def include_bundler(self, bundler: Bundle) -> None:
        """Add bundle of resources, tools and prompts to the server."""
        bundler_tools = bundler.get_tools()
        for tool_name, tool in bundler_tools.items():
            self.add_tool(tool.fn, tool_name, tool.description, tool.annotations)

        bundler_resources, bundler_templates = bundler.get_resources()
        for resource in bundler_resources.values():
            self.add_resource(resource)
        for template_name, template in bundler_templates.items():
            self._resource_manager.add_template(
                template.fn,
                template.uri_template,
                template_name,
                template.description,
                template.mime_type,
            )

        bundler_prompts = bundler.get_prompts()
        for prompt in bundler_prompts.values():
            self.add_prompt(prompt)

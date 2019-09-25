def resource_exists(model, pk):
    """Checks if resource exists."""

    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return False

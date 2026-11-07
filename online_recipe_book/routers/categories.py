import sqlite3
from fastapi import APIRouter, HTTPException
from models.category import CategoryCreate, CategoryResponse
from database import create_connection
router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


# CREATE CATEGORY
@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(category: CategoryCreate):

    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO categories (name) VALUES (?)",
            (category.name,)
        )

        conn.commit()

        category_id = cursor.lastrowid

        cursor.execute(
            "SELECT * FROM categories WHERE id = ?",
            (category_id,)
        )

        result = dict(cursor.fetchone())

        return result

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Category already exists"
        )

    finally:
        conn.close()


# GET ALL CATEGORIES
@router.get("/", response_model=list[CategoryResponse])
def get_categories():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categories")

    categories = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return categories


# GET CATEGORY BY ID
@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM categories WHERE id = ?",
        (category_id,)
    )

    category = cursor.fetchone()

    conn.close()

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return dict(category)


# UPDATE CATEGORY
@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryCreate):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM categories WHERE id = ?",
        (category_id,)
    )

    existing_category = cursor.fetchone()

    if existing_category is None:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    try:
        cursor.execute(
            "UPDATE categories SET name = ? WHERE id = ?",
            (category.name, category_id)
        )

        conn.commit()

        cursor.execute(
            "SELECT * FROM categories WHERE id = ?",
            (category_id,)
        )

        result = dict(cursor.fetchone())

        return result

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Category name already exists"
        )

    finally:
        conn.close()


# DELETE CATEGORY
@router.delete("/{category_id}")
def delete_category(category_id: int):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM categories WHERE id = ?",
        (category_id,)
    )

    category = cursor.fetchone()

    if category is None:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    cursor.execute(
        "DELETE FROM categories WHERE id = ?",
        (category_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Category deleted successfully"}
